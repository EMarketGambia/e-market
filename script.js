// Function for the Wave Payment Alert
function showWave() {
    alert("Please pay D500 to Ebrima at:\nWave: 2071291 or 3679533\n\nAfter payment, keep your Transaction ID and click 'UPLOAD PRODUCT'.");
}

// Connect to your Google Sheet
const SHEET_ID = '1RugKOjvljzdFLPJXEqzHK4EaMU6F-Jodcz-ry2V01Gg';
const SHEET_URL = `https://google.com{SHEET_ID}/gviz/tq?tqx=out:json`;

fetch(SHEET_URL)
    .then(res => res.text())
    .then(data => {
        // Cleaning the Google Sheet data
        const json = JSON.parse(data.substr(47).slice(0, -2));
        const rows = json.table.rows;
        const grid = document.getElementById('market-grid');
        grid.innerHTML = ''; // Removes the "Scanning..." text

        rows.forEach(row => {
            // Getting info from your Sheet columns
            const shop = row.c[1] ? row.c[1].v : "E-Market Vendor";
            const product = row.c[2] ? row.c[2].v : "Item";
            const price = row.c[3] ? row.c[3].v : "0";
            const phone = row.c[4] ? row.c[4].v : "2071291";

            // Creating the Alibaba card for each product
            grid.innerHTML += `
                <div class="card">
                    <img src="https://placeholder.com" alt="Product">
                    <div class="card-info">
                        <strong>${product}</strong>
                        <p class="card-price">D${price}</p>
                        <p style="font-size:10px; color:#666;">Store: ${shop}</p>
                        <a href="https://wa.me{phone}?text=I%20want%20to%20buy%20${product}" class="wa-btn">Order Now</a>
                    </div>
                </div>`;
        });
    })
    .catch(err => {
        console.log("Error loading sheet:", err);
        document.getElementById('market-grid').innerHTML = "Check connection or Sheet permissions.";
    });
