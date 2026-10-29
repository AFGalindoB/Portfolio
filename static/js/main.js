// Reloj en tiempo real
function updateClock() {
  const now = new Date();
  const clockElement = document.getElementById("clock");
  const dateElement = document.getElementById("date");
  
  if (clockElement) {
    clockElement.textContent = now.toLocaleTimeString([], { hour12: false });
  }
  if (dateElement) {
    dateElement.textContent = now.toLocaleDateString([], { weekday: "long", day: "2-digit", month: "long", year: "numeric" });
  }
}

if (document.getElementById("clock")) {
  updateClock();
  setInterval(updateClock, 1000);
}

// Control del carrusel de proyectos
let currentSlide = 0;
function changeProject(direction) {
  const slides = document.querySelectorAll('.project-slide');
  if (slides.length > 0) {
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + direction + slides.length) % slides.length;
    slides[currentSlide].classList.add('active');
  }
}

// Control del desplazamiento manual con flechas
function scrollTools(direction) {
  const container = document.getElementById('toolsContainer');
  if (container) {
    const scrollAmount = 220; 
    container.scrollBy({ left: direction * scrollAmount, behavior: 'smooth' });
  }
}

// Cálculo dinámico del ancho visible en vivo
function updateToolsCarouselWidth() {
  const container = document.getElementById('toolsContainer');
  if (!container) return;

  const itemWidth = 68;
  const gap = 16;
  const parentWidth = container.parentElement.clientWidth;
  const availableWidth = parentWidth - 40; 
  
  let visibleCount = Math.floor(availableWidth / (itemWidth + gap));
  if (visibleCount < 2) visibleCount = 2;
  
  const exactWidth = (visibleCount * itemWidth) + ((visibleCount - 1) * gap);
  container.style.maxWidth = `${exactWidth}px`;
}

// --- AUTO-SCROLL CON ACELERACIÓN, DESACELERACIÓN E INERCIA (1 SEGUNDO DE TRANSICIÓN) ---
let isHovered = false;
let animationFrameId = null;

// Variables de control de velocidad y límites
let currentSpeed = 0;       // Velocidad actual en píxeles por fotograma equivalente
const maxSpeed = 0.5;       // Límite de velocidad máxima (puedes ajustarlo si lo quieres un poco más rápido o lento)
const transitionTime = 1000; // Tiempo de transición en milisegundos (1 segundo)

function startAutoScroll() {
  const container = document.getElementById('toolsContainer');
  const panel = document.getElementById('knowledge');
  if (!container || !panel) return;

  panel.addEventListener('mouseenter', () => {
    isHovered = true; // Al entrar el cursor, la velocidad objetivo será 0 (desaceleración)
  });

  panel.addEventListener('mouseleave', () => {
    isHovered = false; // Al salir el cursor, la velocidad objetivo será maxSpeed (aceleración)
  });

  let scrollPos = container.scrollLeft;
  let lastTime = performance.now();

  function step(currentTime) {
    const deltaTime = currentTime - lastTime;
    lastTime = currentTime;

    // Definir la velocidad meta: si hay hover es 0, si no hay hover es maxSpeed
    const targetSpeed = isHovered ? 0 : maxSpeed;

    // Tasa de cambio por milisegundo para completar la transición exactamente en 1 segundo
    const rate = maxSpeed / transitionTime;
    const speedStep = rate * deltaTime;

    // Ajustar la velocidad actual de forma gradual hacia la velocidad meta (Aceleración / Desaceleración)
    if (currentSpeed < targetSpeed) {
      currentSpeed = Math.min(targetSpeed, currentSpeed + speedStep);
    } else if (currentSpeed > targetSpeed) {
      currentSpeed = Math.max(targetSpeed, currentSpeed - speedStep);
    }

    // Si la velocidad es mayor a 0, movemos el scroll
    if (currentSpeed > 0) {
      scrollPos += currentSpeed;
      
      // Si llega al final del contenedor, regresa al inicio suavemente de forma imperceptible
      if (scrollPos >= container.scrollWidth - container.clientWidth) {
        scrollPos = 0;
      }
      
      container.scrollLeft = scrollPos;
    } else {
      // Si está completamente detenido, sincronizamos con la posición actual por si el usuario hizo scroll manual
      scrollPos = container.scrollLeft;
    }
    
    animationFrameId = requestAnimationFrame(step);
  }

  // Arrancar el ciclo de animación por fotogramas
  animationFrameId = requestAnimationFrame(step);
}

// Inicialización de eventos
window.addEventListener('DOMContentLoaded', () => {
  updateToolsCarouselWidth();
  startAutoScroll();
});

window.addEventListener('resize', updateToolsCarouselWidth);

// ResizeObserver para cambios de tamaño en tiempo real
const knowledgePanel = document.querySelector('.knowledge-panel');
if (knowledgePanel) {
  const resizeObserver = new ResizeObserver(() => {
    updateToolsCarouselWidth();
  });
  resizeObserver.observe(knowledgePanel);
}