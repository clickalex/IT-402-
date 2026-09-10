# IT-402 Study Hub

Static, offline-friendly CBSE Class 10 Information Technology (402), 2026–27 study website for the Domestic Data Entry Operator job role. It uses plain HTML, CSS and vanilla JavaScript with LibreOffice Writer, Calc and Base procedures.

## Folder structure

```text
.
├── index.html and study pages        # publishable site pages
├── assets/css/styles.css              # shared responsive and print styling
├── assets/js/app.js                   # theme, search, progress, quiz and timer
├── content/*.md                       # editable curriculum/content map
└── docs/PROJECT.md                    # suggested student project structure
```

## Run locally

Open `index.html` directly, or run `python3 -m http.server 8000` in this folder and visit `http://localhost:8000`.

## Deploy free

For GitHub Pages, enable **Settings → Pages → Deploy from branch** with the repository root as the publishing directory. Netlify and Vercel need no build command; publish directory is `.`.

## Edit content later

Edit the relevant HTML page for visible content. Use the matching Markdown file in `content/` as the curriculum outline, then update the HTML. Shared appearance is in `assets/css/styles.css`; interactions are in `assets/js/app.js`. Keep relative links and avoid external dependencies. Progress and theme preferences are stored only in the browser.
