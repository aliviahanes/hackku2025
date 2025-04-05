// Select all sections with the "hidden" class
const sections = document.querySelectorAll('.hidden');

// Create an IntersectionObserver
const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Add the "visible" class to the section when it enters the viewport
            entry.target.classList.add('visible');
            // Stop observing the section once it becomes visible
            observer.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.1 // Trigger when 10% of the section is visible
});

// Observe each section
sections.forEach(section => observer.observe(section));