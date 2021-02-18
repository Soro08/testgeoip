# testgeoip

```HTML
<script src='https://cdn.jsdelivr.net/npm/vue/dist/vue.js'></script>
<script src='https://unpkg.com/axios/dist/axios.min.js'></script>

<script>
    var app = new Vue({
        el: '#app',
        data: {
            base_url: window.location.protocol + '//' + window.location.host + '/'
        },
        delimiters:["${", "}"],
        mounted() {
        },
        methods: {
            getMyInfo: function(){
                axios.get(this.base_url + 'api/about/', {
                    headers: {
                        'xsrfHeaderName': 'X-CSRFToken',
                        'xsrfCookieName': 'csrftoken'
                    }
                })
                .then(reponse => {
                    console.log(reponse.data)
                })
                .catch((err) => {
                    console.log(err)
                })
            },
            postMyInfo: function(e) {
                let formData = new FormData();
                formData.append('filed1', '');
                axios.defaults.xsrfCookieName = 'csrftoken';
                axios.defaults.xsrfHeaderName = 'X-CSRFToken';
                axios.post(this.base_url + 'api/contact/', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    }
                })
                .then((response) => {
                    console.log(response.data);
                })
                .catch((err) => {
                    console.log(err);
                })
            },
        }
    })
</script>
```


```PYTHON
    import json
    postdata = json.loads(request.body.decode('utf-8'))
```
