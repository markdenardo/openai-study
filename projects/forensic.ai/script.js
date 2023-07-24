const poisonDetectionBtn = document.getElementById("poisonDetectionBtn");
const poisonDetectionResult = document.getElementById("poisonDetectionResult");
const drugInteractionBtn = document.getElementById("drugInteractionBtn");
const drugInteractionResult = document.getElementById("drugInteractionResult");

const apiBaseUrl = "http://your-api-url.com";

poisonDetectionBtn.addEventListener("click", () => {
  const symptoms = document.getElementById("symptoms").value;
  fetch(`${apiBaseUrl}/poison_detection`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ symptoms }),
  })
    .then((response) => response.json())
    .then((data) => {
      poisonDetectionResult.innerHTML = `<p>Poison Detected: ${data.poison_detected}</p><p>First Aid Instructions: ${data.first_aid_instructions}</p><p>Emergency Contact: ${data.emergency_contact}</p>`;
    })
    .catch((error) => {
      poisonDetectionResult.innerHTML =
        "<p>Error occurred while detecting poison. Please try again later.</p>";
      console.error(error);
    });
});

drugInteractionBtn.addEventListener("click", () => {
  const medications = document.getElementById("medications").value;
  fetch(`${apiBaseUrl}/drug_interaction`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ medications }),
  })
    .then((response) => response.json())
    .then((data) => {
      drugInteractionResult.innerHTML = `<p>Interactions: ${data.interactions.join(
        ", "
      )}</p><p>Warnings: ${data.warnings.join(", ")}</p>`;
    })
    .catch((error) => {
      drugInteractionResult.innerHTML =
        "<p>Error occurred while checking drug interactions. Please try again later.</p>";
      console.error(error);
    });
});
