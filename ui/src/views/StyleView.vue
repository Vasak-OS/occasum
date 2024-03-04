<script lang="ts" setup>
import { inject, ref, onMounted } from 'vue';

const $vsk: any = inject('vsk');
const section = 'STYLE';
const radius = ref(10);
const color = ref('');
const darkMode = ref(false);

const getConfig = (configName: string) => {
  return $vsk.getConfig(section, configName);
};

const setConfig = (configName: string, value: any) => {
  $vsk.setConfig(section, configName, value);
};

onMounted(async () => {
  radius.value = await getConfig('radius');
  color.value = await getConfig('color');
  darkMode.value = await getConfig('darkMode');
});
</script>

<template>
  <div class="occasum-style">
    <div>
      <label for="radius">Radius</label>
      <input
        type="range"
        name="radius"
        min="2"
        max="15"
        v-model="radius"
        @change="setConfig('radius', radius)"
      />
      <span>{{ radius }}</span>
    </div>
    <div>
      <label for="color">Color</label>
      <input
        type="color"
        name="color"
        min="2"
        max="15"
        v-model="color"
        @change="setConfig('color', color)"
      />
      <span>{{ color }}</span>
    </div>
    <div>
      <label for="darkMode">DarkMode</label>
      <input
        type="checkbox"
        name="darkMode"
        v-model="darkMode"
        @change="setConfig('darkMode', darkMode)"
      />
      <span>{{ darkMode }}</span>
    </div>
  </div>
</template>
