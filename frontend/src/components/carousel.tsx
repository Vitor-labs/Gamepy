import React, { useState } from 'react';
import Card from './card';
import styled from 'styled-components';

const CarouselContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
`;

const Carousel = () => {
    const [index, setIndex] = useState(0);
    const products = [
        {
            id: 1,
            name: 'Product 1',
            description: 'This is a description of product 1',
            image: 'https://source.unsplash.com/random/300x300/?1',
        },
        {
            id: 2,
            name: 'Product 2',
            description: 'This is a description of product 2',
            image: 'https://source.unsplash.com/random/300x300/?2',
        },
        {
            id: 3,
            name: 'Product 3',
            description: 'This is a description of product 3',
            image: 'https://source.unsplash.com/random/300x300/?3',
        },
        {
            id: 4,
            name: 'Product 4',
            description: 'This is a description of product 4',
            image: 'https://source.unsplash.com/random/300x300/?4',
        },
        {
            id: 5,
            name: 'Product 5',
            description: 'This is a description of product 5',
            image: 'https://source.unsplash.com/random/300x300/?5',
        },
        {
            id: 6,
            name: 'Product 6',
            description: 'This is a description of product 6',
            image: 'https://source.unsplash.com/random/300x300/?6',
        },
    ];

    const handlePrevious = () => {
        setIndex((prevIndex) => {
            if (prevIndex === 0) {
                return products.length - 1;
            }
            return prevIndex - 1;
        });
    };

    const handleNext = () => {
        setIndex((prevIndex) => (prevIndex + 1) % products.length);
    };

    return (
        <CarouselContainer>
            <Card />
            <div>
                <button onClick={handlePrevious}>Previous</button>
                <button onClick={handleNext}>Next</button>
            </div>
        </CarouselContainer>
    );
};

export default Carousel;
