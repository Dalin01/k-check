import React from 'react';
import { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { getRooms } from '../../state/actionCreators/rooms';

const Home = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getRooms());
  });

  return <>Home</>;
};

export default Home;
