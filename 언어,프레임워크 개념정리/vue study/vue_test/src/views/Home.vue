<template>
    <div>
        <h1>hello home {{title2}}</h1>
        <input type="text" v-model="input1">
        <button type="button" @click="getData()">get</button>
        <button type="button" @click="setData()">set</button>
        <select class="form-control" v-model="region">
            <option :key="i" :value="d.v" v-for="(d,i) in options">{{d.t}}</option>
        </select>
        <table class="table table-bordered" v-if="tableshow">
            <tr :key="i" :value="d.v" v-for="(d,i) in options">
                <td>{{d.v}}</td>
                <td>{{d.t}}</td>
            </tr>

        </table>
    </div>
</template>
<script>
export default {
    data() {
        return {
            title: "개발자의 품격",
            title2: "roqkfwk",
            input1: "abc",
            options: [
                { v: "s", t:"ss"},
                { v: "g", t:"gg"},
                { v: "k", t:"kk"}
                ],
            region: "g",
            tableshow: false
        }
    },
    watch: {
        input1() {
            console.log(this.input1)
        }

    },
    methods: {
        getData() {
            alert(this.input1)
        },
        setData() {
            this.input1 = "12345"
        }
    }
}
</script>