<template>
        <v-toolbar>
            <v-toolbar-side-icon></v-toolbar-side-icon>
            <v-toolbar-title> Find NearBy </v-toolbar-title>
            <v-toolbar-items> 
            <router-link to="/" > <v-btn flat> Hospital</v-btn></router-link> 
            <router-link to="/toilet" ><v-btn flat> Toilets</v-btn></router-link>

            </v-toolbar-items>
            <v-spacer></v-spacer>
            <v-toolbar-items class="hidden-sm-and-down">
            <v-btn flat>Contant</v-btn>
            <v-btn flat>About</v-btn>
            </v-toolbar-items>
        </v-toolbar>
</template>

<script>
export default {

}

</script>