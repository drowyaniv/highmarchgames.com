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
