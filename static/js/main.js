// Simple contact form submission
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault(); // Prevent form submission
            
            // Get form fields
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const subject = document.getElementById('subject').value;
            const message = document.getElementById('message').value;
            
            // Simple validation - check if fields are filled
            if (name && email && subject && message) {
                // Show success message
                alert('Thank you for your message! We will contact you soon.');
                // Clear the form
                contactForm.reset();
            } else {
                // Show error if fields are empty
                alert('Please fill in all fields.');
            }
        });
    }

    // Mobile menu code removed
});
