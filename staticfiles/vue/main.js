var app = new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    results: [],
    categories: []
  },
  mounted: function () {
        this.allItems();
        this.getCategories();
    },
    methods: {
        allItems: async function () {
            let response = await axi.get('items/')
            console.log('salam')
            console.log(response.data['data'])
            this.results = response.data['data']
        },

        getCategories: async function () {
            let response = await axi.get('categories/')
            console.log('salam')
            console.log(response.data['data'])
            this.categories = response.data['data']
        },

        filter: async function (id) {
            let response = await axi.get('items/?subcategory=' + id.toString())
            this.results = response.data['data']
        }
    }
})