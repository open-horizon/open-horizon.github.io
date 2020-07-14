{% assign code = include.code %}
{% assign language = include.language %}

``` {{ language }}
{{ code }}
```
{% assign nanosecond = "now" | date: "%N" %}
<textarea id="code{{ nanosecond }}" style="display:none;">{{ code | xml_escape }}</textarea>
<button id="copybutton{{ nanosecond }}" data-clipboard-target="#code{{ nanosecond }}">
  Copy to clipboard
</button>

<script>
var copybutton = document.getElementById('copybutton{{ nanosecond }}');
var clipboard{{ nanosecond }} = new Clipboard(copybutton);

clipboard{{ nanosecond }}.on('success', function(e) {
    console.log(e);
});
clipboard{{ nanosecond }}.on('error', function(e) {
    console.log(e);
});
</script>