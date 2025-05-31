const lightCanvas = document.getElementById('light-canvas');
const ltx = lightCanvas.getContext('2d');

// Set canvas size
function resizeLightCanvas() {
    lightCanvas.width = window.innerWidth;
    lightCanvas.height = window.innerHeight;
}

resizeLightCanvas();
window.addEventListener('resize', resizeLightCanvas);

// Particle class
class Particle {
    constructor() {
        this.reset();
    }

    reset() {
        this.x = Math.random() * lightCanvas.width;
        this.y = Math.random() * lightCanvas.height;
        this.size = Math.random() * 5 + 1;
        this.speedX = Math.random() * 3 - 1.5;
        this.speedY = Math.random() * 3 - 1.5;
        this.color = `hsla(${Math.random() * 60 + 200}, 70%, 60%, 0.5)`;
    }

    update() {
        this.x += this.speedX;
        this.y += this.speedY;

        if (this.size > 0.2) this.size -= 0.1;
        if (this.x < 0 || this.x > lightCanvas.width || 
            this.y < 0 || this.y > lightCanvas.height || 
            this.size <= 0.2) {
            this.reset();
        }
    }

    draw() {
        ltx.fillStyle = this.color;
        ltx.beginPath();
        ltx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ltx.fill();
    }
}

// Create particle array
const particleCount = 100;
const particles = [];
for (let i = 0; i < particleCount; i++) {
    particles.push(new Particle());
}

// Connection line between particles
function connect() {
    for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
            const dx = particles[i].x - particles[j].x;
            const dy = particles[i].y - particles[j].y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < 100) {
                ltx.beginPath();
                ltx.strokeStyle = `rgba(100, 149, 237, ${0.1 - distance/1000})`;
                ltx.lineWidth = 0.5;
                ltx.moveTo(particles[i].x, particles[i].y);
                ltx.lineTo(particles[j].x, particles[j].y);
                ltx.stroke();
            }
        }
    }
}

// Animation
function animate() {
    if (document.documentElement.getAttribute('data-theme') === 'light') {
        ltx.clearRect(0, 0, lightCanvas.width, lightCanvas.height);
        
        // Draw gradient background
        const gradient = ltx.createLinearGradient(0, 0, lightCanvas.width, lightCanvas.height);
        gradient.addColorStop(0, 'rgba(240, 240, 255, 0.5)');
        gradient.addColorStop(1, 'rgba(255, 255, 255, 0.5)');
        ltx.fillStyle = gradient;
        ltx.fillRect(0, 0, lightCanvas.width, lightCanvas.height);

        // Update and draw particles
        particles.forEach(particle => {
            particle.update();
            particle.draw();
        });

        // Draw connections
        connect();
    }
    requestAnimationFrame(animate);
}

animate(); 