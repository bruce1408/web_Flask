<html>
    <head>
        <title>Hello</title>
        <style>h1 {
        font-size: 48px;
        text-shadow: 3px 3px 3px #666666;
        }</style>
    
    <script>
        function change() {
        document.getElementsByTagName('h1')[0].style.color = '#ff0000';
        }
    </script>
    </head>
<body>
  <h1 onclick="change()">Hello, world!</h1>
</body>
</html>
