export function createFeedback(snapshot, candidateId, action, keep, change) {
  const candidate = snapshot.candidates.find((item) => item.candidate_id === candidateId);
  if (!candidate) throw new Error("이 스냅샷에 없는 후보입니다.");
  if (typeof keep !== "string" || typeof change !== "string") throw new Error("피드백을 글로 입력해 주세요.");
  if ([...keep].length > 2000 || [...change].length > 2000) throw new Error("각 메모는 2,000자 이내로 입력해 주세요.");
  switch (action) {
    case "choose":
      if (change !== "") throw new Error("선택 요청의 변경 메모는 비워 주세요.");
      break;
    case "revise":
      if (!change.trim()) throw new Error("바꿀 점을 입력해 주세요.");
      break;
    default:
      throw new Error("지원하지 않는 피드백 요청입니다.");
  }
  const result = {
    schema_version: 1,
    workflow_id: snapshot.workflow_id,
    expected_revision: snapshot.expected_revision,
    candidate_id: candidate.candidate_id,
    candidate_sha256: candidate.candidate_sha256,
    action,
    keep: keep === "" ? [] : [keep],
    change,
  };
  if (new TextEncoder().encode(JSON.stringify(result)).length > 32768) throw new Error("피드백이 너무 깁니다.");
  return result;
}

export function restoreFeedback(snapshot, raw) {
  try {
    const value = JSON.parse(raw);
    if (!value || typeof value !== "object" || Array.isArray(value)) return null;
    const fields = ["schema_version", "workflow_id", "expected_revision", "candidate_id", "candidate_sha256", "action", "keep", "change"];
    if (Object.keys(value).length !== fields.length || fields.some((field) => !Object.hasOwn(value, field))) return null;
    if (value.schema_version !== 1 || value.workflow_id !== snapshot.workflow_id || value.expected_revision !== snapshot.expected_revision) return null;
    if (!Array.isArray(value.keep) || value.keep.length > 1 || value.keep.some((note) => typeof note !== "string")) return null;
    const candidate = snapshot.candidates.find((item) => item.candidate_id === value.candidate_id);
    if (!candidate || candidate.candidate_sha256 !== value.candidate_sha256) return null;
    return createFeedback(snapshot, value.candidate_id, value.action, value.keep[0] ?? "", value.change);
  } catch (error) {
    if (error instanceof Error) return null;
    throw error;
  }
}

export async function copyFeedback(text, write) {
  try {
    await write(text);
    return { copied: true, text };
  } catch (error) {
    if (error instanceof Error || error instanceof DOMException) return { copied: false, text };
    throw error;
  }
}
