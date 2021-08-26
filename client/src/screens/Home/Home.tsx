import React from 'react';
import { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { getRooms } from '../../state/actionCreators/rooms';
import { Row, Col } from 'react-bootstrap';
import RoomCard from '../../components/RoomCard/RoomCard';

const Home = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getRooms());
  });

  const rooms = [
    {
      id: 1,
      name: '101',
      rating: '0.00',
      numReviews: 0,
      price: '29.99',
      description: 'Room 101',
      category: 'cat1',
      createdAt: '2021-08-25T15:50:33.802225+01:00',
      image: '/images/profile.jfif',
      status: 'm',
      availableAt: null,
      createdBy: 1,
      roomType: 1,
      guest: null,
    },
    {
      id: 2,
      name: '102',
      rating: '0.00',
      numReviews: 0,
      price: '50.00',
      description: 'Room 102',
      category: 'cat2',
      createdAt: '2021-08-25T15:51:18.871571+01:00',
      image: null,
      status: 'm',
      availableAt: null,
      createdBy: null,
      roomType: 2,
      guest: null,
    },
  ];

  return (
    <>
      <h3 className="py-3 mt-3"> Our Rooms </h3>
      <hr />
      <br />
      <Row>
        {rooms.map((room) => (
          <Col sm={12} md={6} lg={4} xl={3}>
            <RoomCard room={room} />
          </Col>
        ))}
      </Row>
    </>
  );
};

export default Home;
