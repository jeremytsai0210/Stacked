from .db import db, environment, SCHEMA, add_prefix_for_prod

class Avatar(db.Model):
    __tablename__ = 'avatars'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    avatar_image = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    is_default = db.Column(db.Boolean, default=False, nullable=False)
    selected = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'), name="fk_avatars_user_id"), nullable=True)

    user = db.relationship('User', back_populates='avatars')

    def to_dict(self):
        return {
            'id': self.id,
            'avatar_image': self.avatar_image,
            'description': self.description,
            'is_default': self.is_default,
            'selected': self.selected,
            'user_id': self.user_id,
        }