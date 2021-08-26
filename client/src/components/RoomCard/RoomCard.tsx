import React from 'react';
import { Card } from 'react-bootstrap';
import { Room } from '../../type/types';
import Rating from '../Rating/Rating';
import './index.css';

function RoomCard({ room }: { room: Room }) {
  return (
    <Card>
      <a href={`/api/room/${room.id}`}>
        <Card.Img src={room.image || ''} />
      </a>
      <Card.Body>
        <a href={`/api/room/${room.id}`}>
          <Card.Title>Room {room.name}</Card.Title>
        </a>
        <Card.Text>
          <div>
            <Rating value={+room.rating} text={'' + room.numReviews}></Rating>
          </div>
        </Card.Text>
        <Card.Text as="h4">${room.price}/night</Card.Text>
      </Card.Body>
    </Card>
  );
}

export default RoomCard;
