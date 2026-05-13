function analyzeSymptoms() {
    fever = document.querySelector("#fever").checked;
    headache = document.querySelector("#headache").checked;
    cough = document.querySelector("#cough").checked;
    stomachache = document.querySelector("#stomachache").checked;
    chestpain = document.querySelector("#chestpain").checked;

    let disease = "Unknown"
    let dept = "Unknown"
    let urgency = "Unknown"

    if (fever && headache) {
        disease = "Flu"
        dept = "General"
        urgency = "Medium"
    }
    else if (chestpain) {
        disease = "Heart Attack"
        dept = "Cardiology"
        urgency = "High"
    }
    else if (fever && cough) {
        disease = "Pneumonia"
        dept = "Respiratory"
        urgency = "High"
    }
    else if (stomachache) {
        disease = "Appendicitis"
        dept = "Gastro"
        urgency = "High"
    }
    result = document.querySelector("#result");
    result.innerHTML = `<div> You may have : ${disease}</div><div> Go to : ${dept}</div><div>Urgency : ${urgency}</div>`
}