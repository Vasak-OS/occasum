import InfoView from '@/views/InfoView.vue';
import StyleView from '@/views/StyleView.vue';

const routers: Array<any> = [
  {
    title: 'Info',
    image: 'Style',
    tag: 'INFO',
    component: InfoView
  },
  {
    title: 'Style',
    image: 'Style',
    tag: 'STYLE',
    component: StyleView
  }
];

export default routers;
