import React from 'react';
import styled from 'styled-components';

const CardContainer = styled.div`
  max-width: 300px;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  background-color: ${props => props.theme.mode === 'dark' ? '#1a202c' : 'white'};
  color: ${props => props.theme.mode === 'dark' ? '#ffffff' : '#000000'};
  display: flex;
  flex-direction: column;
`;

const Image = styled.img`
  object-fit: cover;
  object-position: center;
  width: 100%;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  height: 72px;
  background-color: ${props => props.theme.mode === 'dark' ? '#1a202c' : 'white'};
`;

const Content = styled.div`
  padding: 12px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
`;

const Title = styled.h2`
  font-size: 24px;
  font-weight: 600;
  letter-spacing: 0.2px;
  margin: 0;
`;

const Description = styled.p`
  margin: 0;
`;

const Button = styled.button`
  width: 100%;
  padding: 9px;
  background-color: ${props => props.theme.mode === 'dark' ? '#6B46C1' : 'white'};
  color: ${props => props.theme.mode === 'dark' ? '#ffffff' : '#000000'};
  font-size: 16px;
  font-weight: 600;
  letter-spacing: 0.2px;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const Card = () => (
  <CardContainer>
    <Image src="https://source.unsplash.com/random/300x300/?2" alt="" />
    <Content>
      <div>
        <Title>Donec lectus leo</Title>
        <Description>Curabitur luctus erat nunc, sed ullamcorper erat vestibulum eget.</Description>
      </div>
      <Button type="button">Read more</Button>
    </Content>
  </CardContainer>
);

export default Card;
