"""Reusable page parts that are not tied to one game."""

# Full-size screenshot viewer for any ".gallery" of buttons with data-full / data-caption.
LIGHTBOX_JS = """<dialog class="lightbox" id="lightbox" aria-label="Screenshot">
  <form method="dialog"><button class="close" aria-label="Close">Close &times;</button></form>
  <img alt="" id="lightbox-img"><p id="lightbox-cap"></p>
</dialog>
<script>
(() => {
  const dlg = document.getElementById('lightbox'), img = document.getElementById('lightbox-img'), cap = document.getElementById('lightbox-cap');
  if (!dlg || !dlg.showModal) return;
  document.querySelectorAll('.gallery button').forEach(b => b.addEventListener('click', () => {
    img.src = b.dataset.full; img.alt = b.dataset.caption; cap.textContent = b.dataset.caption; dlg.showModal();
  }));
  dlg.addEventListener('click', e => { if (e.target === dlg) dlg.close(); });
})();
</script>"""

# Every mailto link also copies the address, so a visitor with no mail app set up still gets it.
MAIL_COPY_JS = """<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script>
(() => {
  const toast = document.getElementById('toast');
  let timer;
  document.querySelectorAll('a[href^="mailto:"]').forEach(a => a.addEventListener('click', () => {
    const address = a.getAttribute('href').slice(7).split('?')[0];
    if (!navigator.clipboard) return;
    navigator.clipboard.writeText(address).then(() => {
      toast.textContent = 'Email address copied: ' + address;
      toast.classList.add('show');
      clearTimeout(timer);
      timer = setTimeout(() => toast.classList.remove('show'), 4000);
    }, () => {});
  }));
})();
</script>"""
