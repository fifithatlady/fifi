document.addEventListener('DOMContentLoaded', function () {
    const filterForm = document.getElementById('filter-form');
    const keywordInput = document.getElementById('keyword');
    const locationInput = document.getElementById('location');
    const jobListings = document.getElementById('job-listings');

    function displayJobListings() {
        fetch('jobs.json')
            .then(response => response.json())
            .then(data => {
                jobListings.innerHTML = '';
                data.jobs.forEach(job => {
                    const jobDiv = document.createElement('div');
                    jobDiv.classList.add('job');
                    jobDiv.innerHTML = `
                        <h2>${job.title}</h2>
                        <p>${job.description}</p>
                        <p>Location: ${job.location}</p>
                        <p>Keywords: ${job.keywords.join(', ')}</p>
                    `;
                    jobListings.appendChild(jobDiv);
                });
            })
            .catch(error => console.error('Error fetching job listings:', error));
    }

    displayJobListings();

    filterForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const keyword = keywordInput.value.toLowerCase();
        const location = locationInput.value.toLowerCase();

        displayJobListings();
        if (keyword || location) {
            const jobs = document.querySelectorAll('.job');
            jobs.forEach(job => {
                const jobKeywords = job.querySelector('p:nth-of-type(4)').textContent.toLowerCase();
                const jobLocation = job.querySelector('p:nth-of-type(3)').textContent.toLowerCase();
                if ((!keyword || jobKeywords.includes(keyword)) && (!location || jobLocation.includes(location))) {
                    job.style.display = 'block';
                } else {
                    job.style.display = 'none';
                }
            });
        }
    });
});

