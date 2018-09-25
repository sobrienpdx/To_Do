


var app = new Vue({
    el: '#app',
		delimiters: ['${','}'],
		http: {
        root: 'http://localhost:8000/rest_index/api',
        headers: {
					// Authorization: 'Token c39a04212685d3d4780ed90fab0b6914579f4af7',
					// csrftoken: Cookies.get('csrftoken'),
        },
		},
    data: {
        heading: 'Brain Extender',
        toDos: [],
        textForToDo: '',
				results: [],
				query: '',

    },


    methods: {
			getToDos: function() {
					this.$http.get('todos/')
							.then((response) => {
									this.toDos = response.body;
							})
							.catch((err) => {
									console.log(err);
							});
			},


			addToDo: function() {
				console.log("you tried to add something")
				if (this.textForToDo){
					this.$http.post('todos/', {'text': this.textForToDo, "completed": false})
					.then((response) => {
							this.getToDos();
							this.textForToDo= '';
					})
					.catch((err) => {
							console.log(err);
					});
				}
			},


			removeToDo: function(id) {
				console.log("you tried to remove it");
				this.$http.delete(`todos/${id}/`)
						.then((response) => {
								this.getToDos();
						})
						.catch((err) => {
								console.log(err);
						});
			},


			markDone: function(id, completed) {
				console.log("you tried to mark it done")
				this.$http.patch(`todos/${id}/`, {'completed': !completed})
						.then((response) => {
								this.getToDos();
						})
						.catch((err) => {
								console.log(err);
						});
			},

			search: function() {
				if (this.query != ''){
					let query = this.query
					this.results = this.toDos.filter(function(el) {
						var x = el.text
						return el.text.toLowerCase().indexOf(query.toLowerCase()) > -1;
					})
				}
				else{
					this.results = this.toDos
				}
			},

	},
	mounted: function() {
			this.getToDos();
	}
});
