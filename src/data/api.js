const API_URL = import.meta.env.VITE_API_URL;

export async function sendToModel(inputData) {
  const response = await fetch(`${API_URL}/predict`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: inputData,
    }),
  });

  if (!response.ok) {
    throw new Error("API error: " + response.status);
  }

  return await response.json();
}
