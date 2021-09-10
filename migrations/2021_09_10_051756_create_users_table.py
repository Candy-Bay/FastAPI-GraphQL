from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.timestamps()
            table.string('address', 42)
            table.string('discordID', 18)

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
