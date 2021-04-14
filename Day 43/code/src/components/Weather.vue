<template>
    <div>
        <h3>Day starts on
            {{ weather 
                ? Date(weather['First_UTC']).toLocaleString()
                : 'Choose a day'
            }}</h3>
        <p>Season: {{ weather ? weather['Season'] : 'Choose a day' }}</p>
        <p>Pressure: {{ weather ? weather['PRE'] : 'Choose a day' }}</p>
    </div>
</template>

<script>
export default {
    name: 'Weather',
    props: ['weather']
}
</script>

<style scoped>
</style>