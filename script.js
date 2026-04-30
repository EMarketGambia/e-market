// --- 1. CONFIGURATION ---
const MY_WAVE_NUMBER = "2202071291"; 
const SHEET_ID = '1RugKOjvlJzdFLPJXEqzHK4EaMU6F-Jodcz-ry2V01Gg';
const PAYMENT_LINK = "https://modempay.com"; // Your Wave/Afrimoney payment gateway

// --- 2. AUTOMATED "CHOPLIFE" PAYMENT FLOW ---
function startPostFlow() {
    const userConfirm = confirm("Listing a product costs D500. You will be redirected to Wave to complete payment before posting. Proceed?");
    if (userConfirm) {
        window.location.href = PAYMENT_LINK;
    }
}

// --- 3. ALIBABA LIVE SEARCH ---
document.querySelector('.search-bar').addEventListener('input', (e) => {
    const term = e.target.value.toLowerCase();
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        const title = card.querySelector('strong').innerText.toLowerCase();
        card.style.display = title.includes(term) ? "block" : "none";
    });
});

// --- 4. GOOGLE SHEET DATA INTEGRATION ---
// Corrected the URL format to pull data from your sheet
const SHEET_URL = `https://google.com{SHEET_ID}/gviz/tq?tqx=out:json`;

fetch(SHEET_URL)
    .then(res => res.text())
    .then(data => {
        // Cleaning the Google JSON response
        const json = JSON.parse(data.substring(47).slice(0, -2));
        const rows = json.table.rows;
        const grid = document.getElementById('market-grid');
        grid.innerHTML = ''; // Clear the "Syncing..." message

        rows.forEach(row => {
            // Mapping columns: A=Shop, B=Product, C=Price, D=WhatsApp
            const shop = row.c[0] ? row.c[0].v : "E-Market Vendor";
            const product = row.c[1] ? row.c[1].v : "Item";
            const price = row.c[2] ? row.c[2].v : "Check Price";
            const sellerWA = row.c[3] ? row.c[3].v : MY_WAVE_NUMBER;

            grid.innerHTML += `
                <div class="card" style="border: 1px solid #e0e0e0; border-radius: 12px; margin-bottom: 15px; overflow: hidden; background: #fff; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                    <img src="https://placeholder.com{product}" alt="Product" style="width: 100%; height: 160px; object-fit: cover;">
                    <div style="padding: 12px;">
                        <strong style="font-size: 15px; display: block; height: 35px; overflow: hidden;">${product}</strong>
                        <p style="color: #0056b3; font-weight: bold; font-size: 18px; margin: 8px 0;">D${price}</p>
                        <p style="font-size: 11px; color: #777; margin-bottom: 10px;">Store: ${shop}</p>
                        <a href="https://wa.me{sellerWA}?text=I saw your ${product} on E-Market Gambia" 
                           style="background: #25D366; color: #fff; text-decoration: none; padding: 10px; display: block; text-align: center; border-radius: 6px; font-weight: bold; font-size: 14px;">
                           WhatsApp Seller
                        </a>
                    </div>
                </div>`;
        });
    })
    .catch(err => {
        console.log("Error loading sheet:", err);
        document.getElementById('market-grid').innerHTML = "<p style='padding:20px;'>Check your internet or Sheet permissions.</p>";
    });
