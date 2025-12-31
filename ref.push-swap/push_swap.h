/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 05:02:30 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/02 03:24:42 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdlib.h>
# include <unistd.h>
# include <stdio.h>
# include <stddef.h>
# include <limits.h> 

typedef struct s_stack
{
	long			nbr;
	long			i;
	struct s_stack	*next;
	struct s_stack	*prev;
}	t_stack;

typedef struct s_count_moves
{
	int				from_up;
	int				from_down;
	int				to_up;
	int				to_down;
	t_stack			*node;
	int				count;
}	t_count_moves;

typedef struct s_min_max
{
	long			moves_up;
	long			moves_down;
	long			moves_up_dwn;
	long			moves_dwn_up;
}	t_min_max;

size_t			ft_strlen(const char *s);
int				ft_putstr(char *s);
int				ft_is_space(int c);
long			ft_atoi(const char *str);
void			ft_split_free(char **lst);
char			**ft_split(char *str);
void			*ft_calloc(size_t count, size_t size);
t_stack			*ft_stack_add_new(long *nbr);
void			ft_stack_add_back(t_stack **stack, t_stack *new_node);
void			ft_stack_add_front(t_stack **stack, t_stack *new_node);
t_stack			*ft_stack_remove_first(t_stack **stack);
int				ft_stack_size(t_stack *stack);
void			ft_stack_clear(t_stack **stack);
int				ft_has_duplicates(t_stack *stack);
void			ft_error(void);

void			ft_pa(t_stack **a, t_stack **b, int w);
void			ft_pb(t_stack **a, t_stack **b, int w);
void			ft_ra(t_stack **a, int w);
void			ft_rb(t_stack **b, int w);
void			ft_rr(t_stack **a, t_stack **b, int w);
void			ft_rra(t_stack **a, int w);
void			ft_rrb(t_stack **b, int w);
void			ft_rrr(t_stack **a, t_stack **b, int w);
void			ft_sa(t_stack **a, int w);
void			ft_sb(t_stack **b, int w);
void			ft_ss(t_stack **a, t_stack **b, int w);

t_count_moves	*ft_calc_moves(t_stack **from, t_stack **to, int len_from);
void			ft_execute_calculated_moves(t_stack **from, t_stack **to,
					t_count_moves *moves);
void			ft_execute_rotate_rev(t_stack **from, t_stack **to,
					int from_down, int to_down);
void			ft_execute_rotate(t_stack **from, t_stack **to,
					t_count_moves *moves);
void			ft_ra_rrab(t_stack **from, t_stack **to,
					t_count_moves *moves, int to_size);
void			ft_rra_rb(t_stack **from, t_stack **to,
					t_count_moves *moves, int from_size);
t_min_max		ft_count_moves_final(t_count_moves *moves,
					int to_size, int from_size);
int				ft_count_moves(t_count_moves *moves);
void			ft_stack_total_cost(t_stack **from, t_stack **to,
					t_stack *node, t_count_moves *moves);
t_count_moves	*ft_calc_moves(t_stack **from, t_stack **to, int len_from);

int				ft_validate_number(const char *str);
long			ft_find_min(t_stack *stack);
long			ft_find_max(t_stack *stack);
int				ft_is_sorted(t_stack *stack);
void			ft_assign_index(t_stack **stack);
int				ft_find_position_of_min(t_stack *stack);
void			ft_rotate_to_min(t_stack **stack);
int				ft_find_target_pos(t_stack *stack_b, long value);
int				ft_get_position(t_stack *stack, t_stack *node);

void			ft_sort_three(t_stack **a);
void			ft_sort_small(t_stack **a, t_stack **b);
void			ft_execute_moves_start(t_stack **a, t_stack **b);
#endif