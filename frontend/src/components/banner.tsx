import React from 'react';
import styled from 'styled-components';

const Container = styled.div`
  padding: 1.5rem;
  background-color: #333;
  color: #fff;
  @media (prefers-color-scheme: dark) {
    background-color: #5f2583;
    color: #333;
  }
`;

const InnerContainer = styled.div`
  max-width: 1200px;
  margin: 0 auto;
`;

const FlexContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  @media (min-width: 768px) {
    flex-direction: row;
  }
`;

const Heading = styled.h2`
  text-align: center;
  font-size: 4rem;
  letter-spacing: -0.05em;
  font-weight: bold;
  @media (min-width: 576px) {
    font-size: 6rem;
  }
`;

const SpaceContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem 0;
  @media (min-width: 768px) {
    padding: 0;
  }
`;

const Space = styled.span`
  margin: 0.5rem 0;
`;

const Bold = styled.span`
  font-weight: bold;
  font-size: 1.5rem;
`;

const Button = styled.a`
  padding: 0.5rem 1.5rem;
  margin-top: 1rem;
  @media (min-width: 768px) {
    margin-top: 0;
  }
  border-radius: 1rem;
  border: 1px solid #fff;
  text-decoration: none;
  display: block;
  @media (prefers-color-scheme: dark) {
    background-color: #333;
    color: #fff;
    border-color: #333;
  }
`;

const Banner: React.FC = () => {
  return (
    <Container>
      <InnerContainer>
        <FlexContainer>
          <Heading>
            Up to
            <br className="hidden-sm" />
            50% Off
          </Heading>
          <SpaceContainer>
            <Space>Plus free shipping! Use code:</Space>
            <Bold>GamepySupera</Bold>
          </SpaceContainer>
          <Button href="#" rel="noreferrer noopener">Shop Now</Button>
        </FlexContainer>
      </InnerContainer>
    </Container>
  );
};

export default Banner;
