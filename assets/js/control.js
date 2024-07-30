function updateCountdown() {
    const targetDate = new Date("2024-12-31T23:59:59").getTime();
    const now = new Date().getTime();
    const timeLeft = targetDate - now;

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    document.getElementById('days').innerHTML = `${String(days).padStart(2, '0')}<div class="label">Kun</div>`;
    document.getElementById('hours').innerHTML = `${String(hours).padStart(2, '0')}<div class="label">Soat</div>`;
    document.getElementById('minutes').innerHTML = `${String(minutes).padStart(2, '0')}<div class="label">Minut</div>`;
    document.getElementById('seconds').innerHTML = `${String(seconds).padStart(2, '0')}<div class="label">Soniya</div>`;

    if (timeLeft < 0) {
        document.getElementById('countdown').innerHTML = "EXPIRED";
    }
}

setInterval(updateCountdown, 1000);
updateCountdown(); 
