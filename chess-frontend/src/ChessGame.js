import React, { useState, useEffect } from "react";
import { Chessboard } from "react-chessboard";
import { io } from "socket.io-client";

const socket = new WebSocket("ws://localhost:8000/ws/chess/");

const ChessGame = () => {
  const [gamePosition, setGamePosition] = useState("start");

  useEffect(() => {
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.move) {
        setGamePosition(data.move);
      }
    };
  }, []);

  const handleMove = (move) => {
    socket.send(JSON.stringify({ move }));
    setGamePosition(move);
  };

  return <Chessboard position={gamePosition} onPieceDrop={handleMove} />;
};

export default ChessGame;
