<script lang="ts" setup>
import { SideBar, SideButton, SideSection, WindowFrame } from '@vasakgroup/vue-libvasak';
import routers from '@/routers/index';
import { computed, inject, ref } from 'vue';

var section = ref('INFO');
const $vsk: any = inject('vsk');

const changeSection = (newSection: string) => {
  console.log('changeSection', newSection);
  section.value = newSection;
};

const routerComponent = computed(() => {
  return routers.find((r: any) => r.tag === section.value)?.component;
});

const getImage = (image: string): Promise<string> => {
  return $vsk.getIcon(image);
};

const routersData = ref(routers);

routersData.value.forEach((router: any) => {
  getImage(router.image).then((img: string) => {
    router.image = img;
  });
})

</script>

<template>
  <WindowFrame title="Occasum">
    <div class="container-fluid">
      <div class="row flex-nowarp">
        <SideBar>
          <SideSection>
            <template v-for="router in routersData" :key="router.tag">
              <SideButton
                :title="router.title"
                :image="router.image"
                @click="changeSection(router.tag)"
              />
            </template>
          </SideSection>
          <SideSection>
            <SideButton
              title="Link"
              image="https://via.placeholder.com/32"
              exec="https://google.com"
            />
          </SideSection>
        </SideBar>

        <div class="p-3 col side-content-area">
          <component :is="routerComponent" />
        </div>
      </div>
    </div>
  </WindowFrame>
</template>
