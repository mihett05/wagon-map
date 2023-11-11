import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';
import AccountModal from '~/components/accountModal';
import DispatchersGrid from '~/components/dispatchers';

export default function Account() {

  return (
    <div>
      <Container maxWidth="sm">
        <CssBaseline />
        <AccountModal></AccountModal>
          </Container>
            <DispatchersGrid></DispatchersGrid>


    </div>
  );
}
