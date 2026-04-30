// This function triggers when someone clicks 'Pay with Wave'
function processWavePayment(productName, price) {
    console.log("Starting automation for: " + productName);
    
    // 1. Redirect to your Wave Merchant Link (Replace with your actual link)
    // This part is manual for the customer, but the notification will be auto
    window.location.href = "https://wave.com"; 
    
    // 2. Automated Notification (Simulation)
    // In a real Alibaba setup, your app.py would send the WhatsApp alert 
    // to you automatically once the Wave Webhook confirms the money.
}

// Function to handle the WhatsApp chat button
function chatSeller(product) {
    const myNumber = "2202071291";
    const message = "Hello Ebrima, I am interested in " + product + ". I'm ready to pay via Wave.";
    window.open("https://wa.me" + myNumber + "?text=" + encodeURIComponent(message), "_blank");
}
