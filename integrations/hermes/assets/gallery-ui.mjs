const snapshot = JSON.parse(document.querySelector("#gallery-data").textContent);
const form = document.querySelector("#feedback-form");
const keepInput = document.querySelector("#keep");
const changeInput = document.querySelector("#change");
const actionInput = document.querySelector("#feedback-action");
const output = document.querySelector("#feedback-output");
const copyButton = document.querySelector("#copy-feedback");
const clearButton = document.querySelector("#clear-feedback");
const status = document.querySelector("#feedback-status");
const targetLabel = document.querySelector("#draft-target");
const storageKey = `logopia:feedback:${snapshot.workflow_id}:r${snapshot.expected_revision}`;
let targetId = null;
let storageAvailable = true;

function saveDraft(text) {
  try {
    if (text) localStorage.setItem(storageKey, text);
    else localStorage.removeItem(storageKey);
  } catch (error) {
    if (!(error instanceof Error || error instanceof DOMException)) throw error;
    storageAvailable = false;
  }
}

function updateDraft() {
  if (targetId === null) return;
  try {
    const draft = createFeedback(snapshot, targetId, actionInput.value, keepInput.value, changeInput.value);
    output.value = JSON.stringify(draft, null, 2);
    copyButton.disabled = false;
    saveDraft(output.value);
    status.textContent = storageAvailable
      ? "이 버전의 초안을 이 브라우저에 저장했습니다. 아직 Hermes에 보내지 않았습니다."
      : "브라우저 저장을 사용할 수 없습니다. 페이지를 닫기 전에 초안을 복사해 주세요.";
  } catch (error) {
    if (!(error instanceof Error)) throw error;
    output.value = "";
    copyButton.disabled = true;
    saveDraft("");
    status.textContent = error.message;
  }
}

function activate(candidateId, draft = null, focus = true) {
  const candidate = snapshot.candidates.find((item) => item.candidate_id === candidateId);
  if (!candidate) return;
  targetId = candidateId;
  for (const card of document.querySelectorAll("[data-candidate]")) {
    card.classList.toggle("draft-active", card.dataset.candidate === targetId);
  }
  for (const button of document.querySelectorAll("[data-feedback]")) {
    button.setAttribute("aria-pressed", String(button.dataset.feedback === targetId));
  }
  keepInput.disabled = false;
  actionInput.disabled = false;
  clearButton.disabled = false;
  actionInput.value = draft?.action ?? "revise";
  keepInput.value = draft?.keep.join("\n") ?? candidate.keep.join("\n");
  changeInput.value = draft?.change ?? "";
  changeInput.disabled = actionInput.value === "choose";
  targetLabel.textContent = `피드백 대상 ${targetId} · ${snapshot.workflow_id} · r${snapshot.expected_revision}`;
  updateDraft();
  if (focus) {
    document.querySelector("#feedback").scrollIntoView({ behavior: "instant", block: "start" });
    keepInput.focus({ preventScroll: true });
  }
}

for (const button of document.querySelectorAll("[data-feedback]")) {
  button.setAttribute("aria-pressed", "false");
  button.addEventListener("click", () => {
    if (targetId === button.dataset.feedback) {
      keepInput.focus();
      return;
    }
    activate(button.dataset.feedback);
  });
}
form.addEventListener("submit", (event) => event.preventDefault());
keepInput.addEventListener("input", updateDraft);
changeInput.addEventListener("input", updateDraft);
actionInput.addEventListener("change", () => {
  changeInput.disabled = actionInput.value === "choose";
  if (changeInput.disabled) changeInput.value = "";
  updateDraft();
});
copyButton.addEventListener("click", async () => {
  if (!output.value) return;
  const copied = await copyFeedback(output.value, async (text) => {
    if (!navigator.clipboard?.writeText) throw new Error("Clipboard unavailable");
    await navigator.clipboard.writeText(text);
  });
  if (copied.copied) {
    status.textContent = "초안을 복사했습니다. Hermes에 붙여 넣어 요청해 주세요.";
  } else {
    output.focus();
    output.select();
    status.textContent = "자동 복사를 사용할 수 없습니다. 선택된 초안을 ⌘C 또는 Ctrl+C로 복사해 주세요.";
  }
});
clearButton.addEventListener("click", () => {
  keepInput.value = "";
  changeInput.value = "";
  actionInput.value = "revise";
  changeInput.disabled = false;
  output.value = "";
  copyButton.disabled = true;
  saveDraft("");
  status.textContent = "이 브라우저의 초안을 지웠습니다. 원본과 현재 선택은 그대로입니다.";
  keepInput.focus();
});

try {
  const raw = localStorage.getItem(storageKey);
  const restored = raw ? restoreFeedback(snapshot, raw) : null;
  if (restored) activate(restored.candidate_id, restored, false);
  else if (raw) {
    saveDraft("");
    status.textContent = "저장된 초안이 이 버전·원본과 맞지 않아 불러오지 않았습니다.";
  }
} catch (error) {
  if (!(error instanceof Error || error instanceof DOMException)) throw error;
  storageAvailable = false;
  status.textContent = "브라우저 저장을 사용할 수 없습니다. 작성한 초안을 직접 복사해 주세요.";
}
