from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# Revisão e dependências
revision = '4bedb84a47de'
down_revision = None

branch_labels = None
depends_on = None

# Enum para gêneros
generoenum = postgresql.ENUM(
    'ACAO', 'AVENTURA', 'ANIMACAO', 'ANIME', 'BIOGRAFIA', 'COMEDIA', 'DANCA', 'DOCUMENTARIO',
    'DRAMA', 'ESPIONAGEM', 'FAROESTE', 'FANTASIA', 'FICCAO_CIENTIFICA', 'MUSICAL',
    'FILME_POLICIAL', 'TERROR', 'ROMANCE',
    name='generoenum'
)

def upgrade():
    generoenum.create(op.get_bind(), checkfirst=True)
    op.add_column('filmes', sa.Column('generos', postgresql.ARRAY(generoenum), nullable=False, server_default='{}'))

def downgrade():
    op.drop_column('filmes', 'generos')
    generoenum.drop(op.get_bind(), checkfirst=True)
