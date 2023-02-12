import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

const HeaderContainer = styled.header`
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid;
  border-color: red green blue yellow;
  border-radius: 10px;   
  padding: 1rem;
  background-color: #333;
`;

const Logo = styled.img`
  height: 1rem;
`;

const Nav = styled.nav`
  display: flex;
`;

const NavLink = styled(Link)`
  color: #f1f1f1;
  margin-left: 6rem;
  text-decoration: none;

  &:hover {
    color: #ccc;
  }
`;

const Header: React.FC = () => {
  return (
    <HeaderContainer>
      <Logo src="/frontend/src/assets/logo.png" alt="Logo" />
      <Nav>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/login">Login</NavLink>
        <NavLink to="/store">Store</NavLink>
      </Nav>
    </HeaderContainer>
  );
};

export default Header;
