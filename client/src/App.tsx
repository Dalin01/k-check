import { Switch } from 'react-router-dom';
import { routes } from './routes';
import Header from './components/Header/Header';
import { Container } from 'react-bootstrap';

const App = () => {
  return (
    <>
      <Header />
      <Container>
        <Switch>{routes}</Switch>
      </Container>
    </>
  );
};

export default App;
