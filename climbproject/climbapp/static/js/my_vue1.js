new Vue({
  el: '#app-5',
  data: {
      todos: {"climbs": []}
  },
  mounted() {
    axios
      .get('/climbs/me')
      .then(response => (this.todos = response.data))
    setInterval(function (){
      axios
      .get('/climbs/me')
      .then(response => (this.todos = response.data))
      console.log(this.todos);
    }.bind(this), 10000);
  }
})
