<template>
    <header>
        <h1>{{ title }}</h1>
        <select id="day_picker" v-on:change="dayChanged">
            <option :key="day" v-for="day in days" :value="day">
                Day: {{day}}
            </option>
        </select>
    </header>
</template>

<script>
export default {
    name: 'Header',
    props: {
        title: String,
        days: Array
    },
    methods:{
        dayChanged(){
            this.$emit('day-changed', document.getElementById("day_picker").value)
        }
    },
    emits: ['day-changed']
}
</script>

<style scoped>
    header{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
    select{
        width:200px;
        font-size: 20px;
    }
</style>