import { BrowserRouter as Router, Switch } from 'react-router-dom';
import { routes } from './routes';
import Header from './components/Header/Header';

const App = () => {
  return (
    <>
      <Header />
      <Router>
        <Switch>{routes}</Switch>
      </Router>
    </>
  );
};

export default App;
