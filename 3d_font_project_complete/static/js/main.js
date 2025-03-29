document.getElementById("generateButton").addEventListener("click", async () => {
    const text = document.getElementById("textInput").value || "3D Font";
    const color = document.getElementById("colorPicker").value;
    const size = document.getElementById("sizeSlider").value;

    const response = await fetch("/generate-font", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, color, size })
    });

    if (response.ok) {
        const blob = await response.blob();
        const imageUrl = URL.createObjectURL(blob);
        document.getElementById("outputImage").src = imageUrl;
    } else {
        console.error("Failed to generate the font.");
    }
});
