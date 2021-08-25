import { Route } from 'react-router-dom';
import Home from './screens/Home/Home';

type routeContent = {
  path: string;
  component: () => JSX.Element;
  name: string;
};

const ROUTES: routeContent[] = [
  {
    path: '/',
    component: Home,
    name: 'home',
  },
];

export const routes = ROUTES.map(({ path, component, name }) => {
  return <Route exact path={path} component={component} key={name} />;
});
