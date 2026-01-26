const btn = document.getElementById('startBtn');
const list = document.getElementById('recommendationList');

btn.onclick = async () => {
    list.innerHTML = '';
    const modeSelect = document.getElementById('modeSelect'); // Add a dropdown in HTML
    const valueInput = document.getElementById('valueInput'); // Add an input in HTML

    const response = await fetch('/get_recommendations', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            mode: modeSelect.value,
            value: valueInput.value
        })
    });

    const data = await response.json();
    data.forEach(d => {
        const li = document.createElement('li');
        li.innerText = d;
        list.appendChild(li);
    });
};
