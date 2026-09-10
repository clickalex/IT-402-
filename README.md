# IT-402 Study Hub

Static, offline-friendly CBSE Class 10 Information Technology (402), 2026–27 study website. It uses plain HTML, CSS and vanilla JavaScript, with LibreOffice Writer/Calc/Base procedures.

## Run locally
Open `index.html` directly, or run `python3 -m http.server 8000` in this folder and visit `http://localhost:8000`.

## Deploy free
Push this folder to GitHub and enable **Settings → Pages → Deploy from branch** (root folder). Netlify and Vercel can deploy the repository with no build command and publish directory `.`.

## Edit content
Edit the relevant HTML page; shared appearance is in `styles.css` and interactions are in `app.js`. Keep relative links, avoid external dependencies, and validate pages after changing menu paths. Progress and theme preferences are stored only in the browser.
