const GPU_API_URL = "https://inquiries-firefox-classified-times.trycloudflare.com";

const promptInput =
    document.getElementById("prompt");

const generateBtn =
    document.getElementById("generateBtn");

const statusText =
    document.getElementById("status");

const resultDiv =
    document.getElementById("result");


generateBtn.addEventListener("click", async () => {

    const prompt = promptInput.value.trim();

    if (!prompt) {
        statusText.textContent =
            "Please enter a prompt.";
        return;
    }


    generateBtn.disabled = true;

    generateBtn.textContent =
        "Generating...";

    statusText.textContent =
        "Generating image using Tesla T4...";

    resultDiv.innerHTML = "";


    try {

        const response = await fetch(
            `${GPU_API_URL}/generate`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    prompt: prompt
                })
            }
        );


        if (!response.ok) {

            throw new Error(
                "Failed to generate image."
            );

        }


        const data =
            await response.json();


        // -----------------------------
        // Prompt Information
        // -----------------------------

        const promptInfo =
            document.createElement("div");

        promptInfo.className =
            "prompt-info";


        promptInfo.innerHTML = `

            <div class="prompt-box">

                <h3>Original Prompt</h3>

                <p>
                    ${data.original_prompt}
                </p>

            </div>


            <div class="prompt-box">

                <h3>Enhanced Prompt</h3>

                <p>
                    ${data.enhanced_prompt}
                </p>

            </div>

        `;


        resultDiv.appendChild(
            promptInfo
        );


        // -----------------------------
        // Generated Image
        // -----------------------------

        const image =
            document.createElement("img");


        image.src =
            `data:image/png;base64,${data.image}`;


        image.alt =
            "Generated image";


        resultDiv.appendChild(
            image
        );


        // -----------------------------
        // Generation Time
        // -----------------------------

        const timeInfo =
            document.createElement("div");


        timeInfo.className =
            "generation-time";


        timeInfo.innerHTML = `

            <h3>Generation Time</h3>

            <p>
                ${data.generation_time} seconds
            </p>

        `;


        resultDiv.appendChild(
            timeInfo
        );


        statusText.textContent =
            "Image generated successfully!";


    } catch (error) {

        console.error(error);


        statusText.textContent =
            "Error generating image. Please try again.";

    }


    generateBtn.disabled = false;

    generateBtn.textContent =
        "Generate Image";

});