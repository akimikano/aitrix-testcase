var app = new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    results: [],
    categories: [],
    last_param: ''
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
            this.last_param = ''
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
            this.last_param = '?subcategory=' + id.toString();
        },

        order: async function (ordering_type) {
            let sign = '';
            if (this.last_param.length) {
                sign = '&';
            } else {
                sign = '?';
            }

            let response = await axi.get('items/' + this.last_param + sign + 'ordering=' + ordering_type)
            this.results = response.data['data']
        },
    }
})