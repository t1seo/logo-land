"use strict";

(() => {
  const samples = Array.isArray(window.LOGO_SAMPLES) ? window.LOGO_SAMPLES : [];
  const grid = document.getElementById("sample-grid");
  const filters = document.getElementById("filters");
  const template = document.getElementById("card-template");
  const dialog = document.getElementById("sample-dialog");
  const closeButton = document.getElementById("dialog-close");
  const dialogImage = document.getElementById("dialog-image");
  const dialogNotice = document.getElementById("dialog-image-notice");
  const downloadLinks = document.getElementById("download-links");
  let opener = null;
  let activeSample = null;

  const write = (id, value) => { document.getElementById(id).textContent = value; };
  const exported = (sample) => sample.status === "exported";
  const statusText = (sample) => exported(sample) ? "내보내기 완료" : "생성·내보내기 준비 중";
  const formatValue = (value) => {
    if (value === undefined || value === null || value === "") return "아직 기록되지 않았습니다.";
    if (Array.isArray(value)) return value.map(formatValue).join("\n");
    if (typeof value === "object") return JSON.stringify(value, null, 2);
    return String(value);
  };
  const localPath = (value) => typeof value === "string" && /^items\/[a-zA-Z0-9_-]+\/delivery\/[a-zA-Z0-9_.-]+$/.test(value) ? value : null;

  function renderDownloads(sample, imageAvailable) {
    downloadLinks.replaceChildren();
    const ready = exported(sample) && imageAvailable;
    write("download-note", ready ? "생성한 원본 PNG와 로고 패키지, 사용 가이드입니다." : "결과 이미지와 내보내기가 확인되면 파일을 받을 수 있습니다.");
    for (const [label, path, filename] of [
      ["PNG 원본", sample.image, `${sample.id}-logo.png`],
      ["ZIP 패키지", sample.download, `${sample.id}-logo-package.zip`],
      ["사용 가이드", sample.guide, `${sample.id}-brand-guide.md`],
    ]) {
      const safePath = localPath(path);
      const link = document.createElement(ready && safePath ? "a" : "span");
      link.className = "download-link";
      link.textContent = `${label} ↓`;
      if (ready && safePath) {
        link.href = safePath;
        link.download = filename;
      } else {
        link.setAttribute("aria-disabled", "true");
      }
      downloadLinks.append(link);
    }
  }

  function openSample(sample, index, button) {
    opener = button;
    activeSample = sample;
    write("dialog-index", `STUDY ${String(index + 1).padStart(2, "0")} / ${String(samples.length).padStart(2, "0")}`);
    write("dialog-title", sample.name);
    write("dialog-type", sample.typeLabel);
    write("dialog-request", sample.request);
    write("dialog-prompt", sample.prompt);
    write("dialog-review", formatValue(sample.reviewNotes));
    write("dialog-status", statusText(sample));
    const dimensions = sample.dimensions;
    const size = dimensions && !Array.isArray(dimensions) && typeof dimensions === "object" && dimensions.width && dimensions.height
      ? `${dimensions.width} × ${dimensions.height} px` : formatValue(dimensions);
    const metadata = document.getElementById("dialog-metadata");
    metadata.replaceChildren();
    for (const [label, value] of [
      ["상태", statusText(sample)], ["크기", size], ["배경", sample.background],
      ["선택한 시안", sample.selectedId], ["플러그인 버전", sample.pluginVersion],
      ["생성 등록 시각", sample.generatedAt], ["SHA-256", sample.sha256],
    ]) {
      const term = document.createElement("dt");
      const definition = document.createElement("dd");
      term.textContent = label;
      definition.textContent = formatValue(value);
      metadata.append(term, definition);
    }
    document.getElementById("prompt-details").open = false;
    document.getElementById("inspection-details").open = false;
    dialogImage.hidden = true;
    dialogImage.removeAttribute("src");
    dialogImage.alt = `${sample.name} ${sample.typeLabel} 생성 결과`;
    dialogNotice.hidden = false;
    const path = localPath(sample.image);
    dialogNotice.textContent = exported(sample) ? "결과 이미지를 불러오고 있습니다." : "생성 결과 준비 중입니다. 내보내기가 끝나면 실제 이미지가 표시됩니다.";
    renderDownloads(sample, false);
    dialogImage.onload = () => {
      if (activeSample !== sample) return;
      dialogImage.hidden = false;
      dialogNotice.hidden = true;
      renderDownloads(sample, true);
    };
    dialogImage.onerror = () => {
      if (activeSample !== sample) return;
      dialogImage.hidden = true;
      dialogNotice.hidden = false;
      dialogNotice.textContent = "결과 이미지 파일을 찾을 수 없습니다. 샘플 폴더의 파일을 확인해 주세요.";
      write("dialog-status", "이미지 파일 확인 필요");
      renderDownloads(sample, false);
    };
    if (exported(sample) && path) dialogImage.src = path;
    else if (exported(sample)) dialogNotice.textContent = "결과 이미지 경로를 확인해 주세요.";
    document.body.classList.add("dialog-open");
    dialog.showModal();
    dialog.scrollTop = 0;
    closeButton.focus({ preventScroll: true });
  }

  function makeCard(sample, index, order) {
    const card = template.content.firstElementChild.cloneNode(true);
    const button = card.querySelector(".card-open");
    const image = card.querySelector(".card-image");
    const notice = card.querySelector(".image-notice");
    const state = card.querySelector(".card-status");
    card.dataset.status = sample.status;
    card.style.setProperty("--card-order", String(order));
    card.querySelector(".card-name").textContent = sample.name;
    card.querySelector(".card-type").textContent = sample.typeLabel;
    card.querySelector(".card-request").textContent = sample.request;
    card.querySelector(".card-index").textContent = String(index + 1).padStart(2, "0");
    state.textContent = statusText(sample);
    button.setAttribute("aria-label", `${sample.name}, ${sample.typeLabel}, ${statusText(sample)}. 요청과 결과 보기`);
    button.addEventListener("click", () => openSample(sample, index, button));
    const path = localPath(sample.image);
    if (exported(sample) && path) {
      notice.querySelector(".image-notice-text").textContent = "결과 이미지 불러오는 중";
      image.hidden = false;
      image.onload = () => { image.dataset.loaded = "true"; notice.hidden = true; };
      image.onerror = () => {
        image.hidden = true;
        notice.hidden = false;
        card.dataset.imageState = "error";
        notice.querySelector(".image-notice-text").textContent = "결과 이미지 파일 확인 필요";
        state.textContent = "이미지 파일 확인 필요";
        button.setAttribute("aria-label", `${sample.name}, ${sample.typeLabel}, 이미지 파일 확인 필요. 요청 보기`);
      };
      image.src = path;
    } else if (exported(sample)) {
      card.dataset.imageState = "error";
      notice.querySelector(".image-notice-text").textContent = "결과 이미지 경로 확인 필요";
      state.textContent = "이미지 경로 확인 필요";
      button.setAttribute("aria-label", `${sample.name}, ${sample.typeLabel}, 이미지 경로 확인 필요. 요청 보기`);
    }
    return card;
  }

  function filterSamples(label) {
    grid.replaceChildren();
    let count = 0;
    samples.forEach((sample, index) => {
      if (label !== null && sample.typeLabel !== label) return;
      grid.append(makeCard(sample, index, count));
      count += 1;
    });
    for (const button of filters.children) button.setAttribute("aria-pressed", String(button.dataset.filter === (label ?? "")));
    write("result-count", `${label ?? "전체"} · ${count}개 샘플`);
    document.getElementById("empty-state").hidden = count !== 0;
  }

  const labels = [null, ...new Set(samples.map((sample) => sample.typeLabel))];
  for (const label of labels) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "filter-button";
    button.dataset.filter = label ?? "";
    button.setAttribute("aria-controls", "sample-grid");
    button.textContent = label ?? "전체";
    const count = document.createElement("span");
    count.className = "filter-count";
    count.textContent = String(label === null ? samples.length : samples.filter((sample) => sample.typeLabel === label).length).padStart(2, "0");
    button.append(count);
    button.addEventListener("click", () => filterSamples(label));
    filters.append(button);
  }
  write("export-count", `${samples.filter(exported).length} / ${samples.length} 내보내기 완료`);
  filterSamples(null);
  closeButton.addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (event) => {
    const rect = dialog.getBoundingClientRect();
    if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
  });
  dialog.addEventListener("close", () => {
    activeSample = null;
    document.body.classList.remove("dialog-open");
    opener?.focus({ preventScroll: true });
  });
})();
