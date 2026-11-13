# Black Swan Student Society website

The site is a single self-contained page: `index.html`. All styles, scripts and images are inside it, so it can be hosted anywhere that serves static files (GitHub Pages, Netlify, Vercel, Cloudflare Pages).

## Publishing with GitHub Pages

1. Push this folder to a GitHub repository.
2. In the repository, open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, select `main` and `/ (root)`, then **Save**.
4. After a minute the site is live at `https://<your-username>.github.io/<repo-name>/`.

## Editing the site

The page is generated from the files in `source/`. Edit the text or styles there, then rebuild:

```bash
cd source
python3 build2.py
cp preview-local.html ../index.html
```

Commit and push; GitHub Pages republishes automatically.

Where things live:

| File | Content |
| --- | --- |
| `build2.py` | Header menu, page assembly |
| `hero4.py`, `hero4.css` | Homepage video hero, Who we are, cards, divisions |
| `perf.py` | Homepage performance tracker |
| `team.py` | Board, bios, analysts, LinkedIn links |
| `introp.py`, `philo.py`, `values.py` | Introduction, Philosophy and process, Our values |
| `divpage.py` | The five division pages |
| `trk.py` | Track record page |
| `pubs.py` | Investment Research and Market Perspectives |
| `events.py` | Events page |
| `apply.py` | Apply page |
| `footer.py` | Footer |
| `team/` | Board portraits |

## Before launch

- Replace the board portraits and page images with the original files (current ones were captured from screenshots).
- Add the event photos in `events.py`.
